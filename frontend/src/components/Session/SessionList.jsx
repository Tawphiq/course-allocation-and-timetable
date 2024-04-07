import Footer from "../Footer/Footer";
import Header from "../Header/Header";
import Level from "./Session";
import "./Session.css";

const LevelList = () => {
  return (
    <>
      <div>
        <Header />
        <div className="levels-container">
          <Level />
        </div>

        <Footer />
      </div>
    </>
  );
};
export default LevelList;
