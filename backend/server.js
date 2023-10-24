const express = require("express");
const multer = require("multer");
const ExcelJS = require("exceljs");
const puppeteer = require("puppeteer");
const app = express();
const cors = require("cors");
const port = 3000;
const { chromium } = require("playwright");

app.use(cors());

const storage = multer.diskStorage({
  destination: "uploads/",
  filename: function (req, file, callback) {
    callback(null, file.originalname);
  },
});

const upload = multer({ storage: storage });

app.post("/upload", upload.single("excelFile"), async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: "No file uploaded." });
    }

    const workbook = new ExcelJS.Workbook();
    await workbook.xlsx.readFile(`uploads/${req.file.originalname}`);

    const worksheet = workbook.getWorksheet(1);

    const data = [];
    const userMessage = req.body.wamessage;
    console.log(userMessage);
    worksheet.eachRow({ includeEmpty: false, firstRow: 2 }, (row) => {
      console.log(row.values);
      const [et, name, number, date, time] = row.values;
      if (name && number && date && time && name.toLowerCase() != "name") {
        const formattedNumber = "+91" + number;
        data.push([name, formattedNumber, date, time]);
      } else {
        console.error(
          "Skipping a row due to missing or incorrectly formatted data:"
        );
      }
    });

    console.log("Data");
    console.log(data);
    const browser = await chromium.launch();
    for (const [name, number, date, time] of data) {
      if (name && date && time) {
        const message = userMessage
          .replace("NAME", name)
          .replace("DATE", date)
          .replace("TIME", time);

        console.log(message);
        // Navigate to the WhatsApp Web
        const context = await browser.newContext();
        const waLink = `https://wa.me/${number}`;
        console.log(waLink);
        const page = await context.newPage();
        await page.goto(waLink);

        await new Promise((resolve) => setTimeout(resolve, 10000));

        await page.waitForSelector("._1awRl");

        await page.type("._1awRl", message);
        await page.press("._1awRl", "Enter");

        await new Promise((resolve) => setTimeout(resolve, 2000));
        await context.close();
      } else {
        console.error("Skipping a row due to missing data:");
      }
    }

    await browser.close();

    res.send("File uploaded and data extracted successfully!");
  } catch (error) {
    console.error("Error processing Excel file:", error);
    res.status(500).json({ error: "Error processing the uploaded file." });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
