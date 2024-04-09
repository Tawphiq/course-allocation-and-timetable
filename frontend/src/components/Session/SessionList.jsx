import { Link } from "react-router-dom";
import Footer from "../Footer/Footer";
import Header from "../Header/Header";
import Session from "./Session";
import "./Session.css";
import { MdKeyboardBackspace } from "react-icons/md";

const SessionList = () => {
  return (
    <>
      <div>
        <Header />
        <div>
          <Link to="/program-list">
            <button className="flex gap-1 items-center border bg-slate-200 px-3 py-1 m-2 hover:bg-slate-100 rounded-sm">
              <MdKeyboardBackspace />
              Back
            </button>
          </Link>
        </div>
        <div className="levels-container">
          <Session />
        </div>

        <Footer />
      </div>
    </>
  );
};
export default SessionList;
