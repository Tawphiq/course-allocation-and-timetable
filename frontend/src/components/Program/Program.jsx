import { Link } from "react-router-dom";

const Program = () => {
  return (
    <>
      <div className="programs flex flex-col gap-10 lg:text-xl ">
        <div className="program">
          <div className="program-header bg-blue-200 w-2/6 border-8 border-red-400 rounded-tl-md rounded-tr-md">
            <h1 className="text-center">DIPLOMA</h1>
          </div>
          <div className="levels text-center lg:w-3/4 lg:mx-auto  flex flex-col items-center bg-blue-200 border border-red-400 rounded-bl-md rounded-br-md rounded-tr-md shadow-lg">
            <Link
              to="/session-list"
              className="level w-full lg:h-16 lg:py-4 lg:hover:bg-red-900 lg:hover:text-white border-4 border-red-400 py-2 cursor-pointer"
            >
              <div>
                <h2>Level 100</h2>
              </div>
            </Link>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-red-900 lg:hover:text-white border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 200</h2>
            </div>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-red-900 lg:hover:text-white border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 300</h2>
            </div>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-red-900 lg:hover:text-white border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 400</h2>
            </div>
          </div>
        </div>
        <div className="program">
          <div className="program-header bg-blue-200 w-2/6 border-8 border-blue-950 rounded-tl-md rounded-tr-md">
            <h1 className="text-center">DEGREE</h1>
          </div>
          <div className="levels text-center lg:w-3/4 lg:mx-auto   flex flex-col items-center bg-blue-200 border border-blue-950 rounded-bl-md rounded-br-md rounded-tr-md shadow-lg">
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-blue-900 lg:hover:text-white border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 100</h2>
            </div>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-blue-900 lg:hover:text-white border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 200</h2>
            </div>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-blue-900 lg:hover:text-white border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 300</h2>
            </div>
            <div className="level w-full lg:h-16 lg:py-4 lg:hover:bg-blue-900 lg:hover:text-white border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 400</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Program;
