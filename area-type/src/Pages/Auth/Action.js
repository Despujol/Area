import React, { useState } from "react";
import "../Commons.css";
import "./Auth.css";
import Bar from '../Bar'

/**
 * 
 * @param {*} props 
 * Action page qui affiche toute les actions disponibles pour l'utilisateur connecté.
 * L'utilisateur peut cliquer sur une action pour la sélectionner afin de sans servir pour une area
 * @returns 
 */

export const Action = (props) => {
    const [actions, setActions] = useState({});
    const handleClick = (action) => {
        localStorage.setItem('action', JSON.stringify(action));
        if (action.parameters)
            localStorage.setItem('parameters', JSON.stringify({'parameters': action.parameters, 'type': action.type}));
        else
            localStorage.setItem('parameters', JSON.stringify({'parameters': [], 'type': action.type}));
    };
    fetch('http://localhost:8000/getactions/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        },
        body: JSON.stringify({email: JSON.parse(localStorage.getItem('email'))})

    })
    .then(response => response.json())
    .then(data => {
        setActions(data.actions);
        console.log(actions)
    });

    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>All Actions</h2>
                <form className="login-form">
                <ul>
                    {
                        Object.keys(actions).map((key) => (
                        <li key={key}>
                            <strong>[{actions[key].service}] <a href='./option_action' onClick={() => handleClick(actions[key])}>{actions[key].title}</a></strong>: {actions[key].description}
                        </li>
                        ))
                    }
                </ul>
                </form>
            </div>

        </header>
    )
}

export default Action;