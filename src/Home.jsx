import React from "react";

const Home = () => {
  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("excelFile", event.target.excelFile.files[0]);
    formData.append("wamessage", event.target.wamessage.value);

    try {
      const response = await fetch("http://localhost:3000/upload", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log("Success");
      } else {
        console.log("Error");
      }
    } catch (error) {
      // Handle network or request error
    }
  };
  return (
    <div className="home h-screen w-full flex flex-col justify-center">
      <div className="heading text-center">
        <h1 className="montserrat text-4xl font-extrabold leading-none tracking-tight text-green-500 md:text-5xl lg:text-6xl">
          <mark className="bg-white text-green-500 rounded">Automate</mark>
          <mark className=" text-white bg-green-500 rounded">Whapp</mark>
        </h1>
        <p className="mt-1 raleway text-lg font-normal text-black italic lg:text-xl lowercase">
          Transform Your WhatsApp Messaging Experience with Streamlined
          Automation and Personalization
        </p>
        <hr className="w-48 h-1 mx-auto my-4 bg-green-500 border-0 rounded md:my-1" />
      </div>
      <form onSubmit={handleSubmit}>
        <div className="excel text-center flex justify-center mt-8">
          <div className="flex items-center justify-center w-3/4 px-4 raleway">
            <label
              htmlFor="dropzone-file"
              className="flex flex-col items-center justify-center w-full h-fit border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-300 hover:border-white"
            >
              <div className="flex flex-col items-center justify-center pt-5 pb-6">
                <svg
                  className="w-8 h-8 mb-4 text-gray-500 "
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 16"
                >
                  <path
                    stroke="currentColor"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                  />
                </svg>
                <p className="mb-2 text-sm text-gray-500 ">
                  <span className="font-semibold">Click to upload</span> or drag
                  and drop
                </p>
                <p className="text-xs text-gray-500  ">
                  Excel w/ [Name, Number, Time & Date]
                </p>
              </div>

              <input
                id="dropzone-file"
                name="excelFile"
                type="file"
                className="hidden"
              />
            </label>
          </div>
        </div>

        <div className="text-input flex justify-center items-center">
          <div className="sample-message px-4 w-4/5 mt-5 montserrat text-center">
            <label
              htmlFor="message"
              className="block mb-1 text font-medium text-gray-900 "
            >
              Enter the{" "}
              <span className="text-black bg-green-500 rounded-xl">
                WhatsApp
              </span>{" "}
              message to be sent!.
            </label>
            <textarea
              id="message"
              name="wamessage"
              rows="6"
              className="block p-2.5 w-full text-sm text-green-500 font-medium bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 "
              placeholder="Write a message with variables capitalized..."
            ></textarea>
          </div>
        </div>

        <div className="send-message items-center justify-center flex raleway mt-8">
          <button
            type="submit"
            className="text-black button bg-gradient-to-br from-yellow-300 to-green-400  transition duration-300 ease-in  focus:ring-4 focus:outline-none focus:ring-green-200 font-medium rounded-xl text-lg px-16 py-1 text-center mr-2 mb-2"
          >
            Send BULK messages!
          </button>
        </div>
      </form>
    </div>
  );
};

export default Home;
