import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { GoogleOAuthProvider } from '@react-oauth/google';
import ReactDOM from 'react-dom/client';
import './index.css';
import Home from './Pages/Home';
import reportWebVitals from './reportWebVitals';
import { Register } from './Pages/Auth/Register';
import { Login } from './Pages/Auth/Login';
import { Service } from './Pages/Auth/Service';
import { Area } from './Pages/Auth/Area';
import { Action } from './Pages/Auth/Action';
import { Reaction } from './Pages/Auth/Reaction';
import { OptionAction } from './Pages/Auth/Option_action';

/**
 * Fichier qui permet de gérer les routes de l'application
 * Rajouter dans <BrowserRouter> les routes que vous voulez
 * @returns 
 */

export default function App(){
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}></Route>
        <Route path='/register' element={<Register />}></Route>
        <Route path='/login' element={<Login />}></Route>
        <Route path='/service' element={<Service />}></Route>
        <Route path='/area' element={<Area />}></Route>
        <Route path='/action' element={<Action />}></Route>
        <Route path='/reaction' element={<Reaction />}></Route>:
        <Route path='/option_action' element={<OptionAction />}></Route>
      </Routes>
    </BrowserRouter>
  );

}

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <GoogleOAuthProvider clientId="102131040763-ll7a0g7v8d72trbd12kshr2ubh6qdnl7.apps.googleusercontent.com">
    <App />
  </GoogleOAuthProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
