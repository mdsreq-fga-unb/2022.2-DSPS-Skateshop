import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "../pages/Home";

function RoutesComponent(): JSX.Element {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
    </Routes>
  );
}

export default RoutesComponent;
