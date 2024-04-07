const Header = () => {
  return (
    <>
      <header className="bg-blue-100">
        <img
          src="https://dev.upsa.edu.gh/wp-content/uploads/2023/03/upsa-logo-new.png"
          alt="upsa_logo"
          className="w-2/5 h-16"
        />
        <div className="h-14 bg-blue-900 flex items-center justify-center">
          <h1 className="text-xl text-white font-bold text-center uppercase">
            2023/2024 academic year
          </h1>
        </div>
      </header>
    </>
  );
};
export default Header;
