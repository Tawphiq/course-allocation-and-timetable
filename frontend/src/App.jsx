import { Routes, Route } from "react-router-dom";
import Home from "./components/Home/Home";
import ProgramList from "./components/Program/ProgramList";
import SessionList from "./components/Session/SessionList";


function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/program-list" element={<ProgramList />} />
        <Route path="/session-list" element={<SessionList />} />
      </Routes>
    </>
  );
}

export default App;
