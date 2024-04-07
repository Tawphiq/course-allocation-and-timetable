/* eslint-disable react/prop-types */
const Department = () => {
  return (
    <>
      <div className="department w-full h-10 flex justify-center items-center bg-slate-100 text-blue-900 rounded-sm shadow-lg lg:cursor-pointer lg:hover:bg-blue-900 lg:hover:text-white">
        <h1 className="font-semibold text-xl ">IT & Communication Studies</h1>
      </div>
      <div className="department w-full h-10 flex justify-center items-center bg-slate-100 text-blue-900 rounded-sm shadow-lg lg:cursor-pointer lg:hover:bg-blue-900 lg:hover:text-white">
        <h1 className="font-semibold text-xl ">Management Studies</h1>
      </div>
      <div className="department w-full h-10 flex justify-center items-center bg-slate-100 text-blue-900 rounded-sm shadow-lg lg:cursor-pointer lg:hover:bg-blue-900 lg:hover:text-white">
        <h1 className="font-semibold text-xl ">Accounting & Finance</h1>
      </div>
      <div className="department w-full h-10 flex justify-center items-center bg-slate-100 text-blue-900 rounded-sm shadow-lg lg:cursor-pointer lg:hover:bg-blue-900 lg:hover:text-white">
        <h1 className="font-semibold text-xl ">
          Office of Doctoral Programmes
        </h1>
      </div>
    </>
  );
};
export default Department;
