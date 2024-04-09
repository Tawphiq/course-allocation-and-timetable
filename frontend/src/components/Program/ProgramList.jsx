import { Link } from "react-router-dom";
import Footer from "../Footer/Footer";
import Header from "../Header/Header";
import Program from "./Program";
import "./Program.css";
import { MdKeyboardBackspace } from "react-icons/md";

const ProgramList = () => {
  return (
    <>
      <div>
        <Header />
        <div>
          <Link to="/">
            <button className="flex gap-1 items-center border bg-slate-200 px-3 py-1 m-2 lg:m-5 lg:text-lg hover:bg-slate-100 rounded-sm">
              <MdKeyboardBackspace />
              Back
            </button>
          </Link>
        </div>
        <div className="program-list">
          <Program />
        </div>

        <Footer />
      </div>
    </>
  );
};
export default ProgramList;
