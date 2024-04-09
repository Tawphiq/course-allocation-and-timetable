import "./Footer.css";

const Footer = () => {
  return (
    <>
      <footer className="bg-blue-900 text-white md:text-sm lg:text-xl flex justify-center gap-6 md:gap-20 lg:gap-36">
        <div>
          <ul className="flex flex-col gap-2 ">
            <li>
              <a href="https://upsasip.com/">Students Portal</a>
            </li>
            <li>
              <a href="https://upsa.edu.gh/students/student-services/">
                Student Services
              </a>
            </li>
            <li>
              <a href="https://upsa.edu.gh/#">Freshmen Guidelines</a>
            </li>
            <li>
              <a href="https://src.upsa.edu.gh/">The SRC</a>
            </li>
          </ul>
        </div>
        <div>
          <ul className="flex flex-col gap-2">
            <li>
              <a href="https://upsa.edu.gh/students/sports/">
                Sports and Recreation
              </a>
            </li>
            <li>
              <a href="https://upsa.edu.gh/students/counseling-unit/">
                Counselling Unit
              </a>
            </li>
            <li>
              <a href="https://upsahostels.com/">Hostels</a>
            </li>
            <li>
              <a href="https://upsaenterprise.com/">UEIC</a>
            </li>
          </ul>
        </div>
      </footer>
      <div className="text-white lg:text-lg bg-blue-900 pb-2">
        <p className="text-center">@2024 UPSA-Ghana</p>
      </div>
    </>
  );
};
export default Footer;
