// import React from 'react';
import About from '../pages/About';
import Home from '../pages/Home';
import { Routes,Route } from 'react-router-dom';
import Layout from '../pages/Layout';
import Contact from '../pages/Contact';

const MainRouter = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path='/About' element={<About />}/>
        <Route path='/Contact' element={<Contact />}/>
        <Route path='/Layout' element={<Layout />}/>
        {/* Add more routes as needed */}
      </Routes>
    
     
    </div>
  );
}

export default MainRouter;
