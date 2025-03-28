import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Register from "./components/Register";
import Users from "./components/Users";
import Userposts from "./components/Userposts";
import PostComments from "./components/Postcomments";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Register />} />
          <Route path="/users" element={<Users />} />
          <Route path="/posts" element={<Userposts/>}/>
          <Route path="/comments" element={<PostComments/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;
