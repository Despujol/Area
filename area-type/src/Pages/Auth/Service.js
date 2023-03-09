import React, { useState } from "react";
import "../Commons.css";
import "./Auth.css";
import Bar from '../Bar';


/**
 * 
 * @param {*} props 
 * Service page qui affiche toute les services disponibles pour l'utilisateur connecté.
 * Permet aussi a l'utilisateur de se connecter a un service et d'accéder a la page des areas
 * @returns 
 */

export const Service = (props) => {
    const [services, setServices] = useState({});

    localStorage.setItem('action', JSON.stringify({}));
    localStorage.setItem('reaction', JSON.stringify({}));
    if (JSON.parse(localStorage.getItem('email'))) {
        fetch('http://localhost:8000/checkservices/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
            },
            body: JSON.stringify({email: JSON.parse(localStorage.getItem('email'))})
        })
        .then(response => response.json())
        .then(data => {
            setServices(data);
        });
    }
    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>All Service</h2>
                <form className="login-form">
                <div>
                    {
                        Object.keys(services).map((key) => (
                        <div>
                            {key}{services[key] ? ' Connected' : <a href='./'>'Not connected'</a>}
                        </div>
                        ))
                    }
                </div>
                </form>
            </div>
            <h2><a href='/area'>Create an area</a></h2>
        </header>
    )
}

export default Service;