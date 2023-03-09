// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

/**
 * Fichier de configuration de firebase afin de pouvoir se connecter en Oauth avec les providers
 */

const firebaseConfig = {
  apiKey: "AIzaSyBsnCKEBtHkzhWrqGTBLzPEG3GXlpVBC68",
  authDomain: "area-376013.firebaseapp.com",
  projectId: "area-376013",
  storageBucket: "area-376013.appspot.com",
  messagingSenderId: "102131040763",
  appId: "1:102131040763:web:a7dbe867698c2460364b5e",
  measurementId: "G-F7DESXG7MQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

export default auth;