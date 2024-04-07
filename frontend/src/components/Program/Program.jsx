const Program = () => {
  return (
    <>
      <div className="programs flex flex-col gap-10">
        <div className="program">
          <div className="program-header bg-blue-200 w-2/6 border-8 border-red-400 rounded-tl-md rounded-tr-md">
            <h1 className="text-center">DIPLOMA</h1>
          </div>
          <div className="levels text-center  flex flex-col items-center bg-blue-200 border border-red-400 rounded-bl-md rounded-br-md rounded-tr-md shadow-lg">
            <div className="level w-full border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 100</h2>
            </div>
            <div className="level w-full border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 200</h2>
            </div>
            <div className="level w-full border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 300</h2>
            </div>
            <div className="level w-full border-4 border-red-400 py-2 cursor-pointer">
              <h2>Level 400</h2>
            </div>
          </div>
        </div>
        <div className="program">
          <div className="program-header bg-blue-200 w-2/6 border-8 border-blue-950 rounded-tl-md rounded-tr-md">
            <h1 className="text-center">DEGREE</h1>
          </div>
          <div className="levels text-center  flex flex-col items-center bg-blue-200 border border-blue-950 rounded-bl-md rounded-br-md rounded-tr-md shadow-lg">
            <div className="level w-full border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 100</h2>
            </div>
            <div className="level w-full border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 200</h2>
            </div>
            <div className="level w-full border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 300</h2>
            </div>
            <div className="level w-full border-4 border-blue-950 py-2 cursor-pointer">
              <h2>Level 400</h2>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
export default Program;
