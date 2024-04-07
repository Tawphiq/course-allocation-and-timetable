import Footer from "../Footer/Footer";
import Header from "../Header/Header";
import Program from "./Program";
import "./Program.css";

const ProgramList = () => {
  return (
    <>
      <div>
        <Header />
        <div className="program-list">
          <Program />
        </div>

        <Footer />
      </div>
    </>
  );
};
export default ProgramList;
