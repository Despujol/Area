import React, { useState } from "react";
import Bar from "../Bar";


/**
 * 
 * @param {*} props 
 * Page des option pour les actions et reactions. Permet de choisir les paramètres de l'action ou de la reaction afin de les créer
 * @returns 
 */

export const OptionAction = (props) => {

    if (JSON.parse(localStorage.getItem('parameters')).parameters.length === 0) {
        if (JSON.parse(localStorage.getItem('parameters')).type === 'action') {
            localStorage.setItem('action', JSON.stringify({...JSON.parse(localStorage.getItem('action')), parameters: {}}));
            window.location.href = './area';
        } else {
            localStorage.setItem('reaction', JSON.stringify({...JSON.parse(localStorage.getItem('reaction')), parameters: {}}));
            window.location.href = './area';
        }
    }

    const titles = JSON.parse(localStorage.getItem('parameters')).parameters.split(', ');
    const [params, setParams] = useState(Array.from({length: titles.length}, () => ""));

    const handleSubmit = (event) => {
        var res = {};
        for (let i = 0; i < params.length; i++) {
            res[titles[i]] = params[i];
        }
        if (JSON.parse(localStorage.getItem('parameters')).type === 'action') {
            localStorage.setItem('action', JSON.stringify({...JSON.parse(localStorage.getItem('action')), parameters: res}));
            console.log(JSON.parse(localStorage.getItem('action')));
            window.location.href = './area';
        } else {
            localStorage.setItem('reaction', JSON.stringify({...JSON.parse(localStorage.getItem('reaction')), parameters: res}));
            console.log(JSON.parse(localStorage.getItem('reaction')));
            window.location.href = './area';
        }
    }

    const handleInputChange = (index, event) => {
        const newValues = [...params];
        newValues[index] = event.target.value;
        setParams(newValues);
    };

    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>Login</h2>
                <div>
                    {
                        titles.map((value, index) => (
                            <div key={index}>
                                <label key={index}>{value}</label>
                                <input key={index} value={params[index]} onChange={(event) => handleInputChange(index, event)} />
                            </div>
                        ))
                    }
                </div>
                <button className="btn" onClick={handleSubmit}>Submit</button>
            </div>
        </header>
    );
};

export default OptionAction;
