import { signInWithPopup, OAuthProvider } from "firebase/auth";
import auth from './../firebase';


const microsoftLogin = async () => {
    const provider = new OAuthProvider('microsoft.com');
    provider.addScope('profile, offline_access, Calendars.ReadWrite, Mail.Send, User.Read');
    await signInWithPopup(auth, provider)
    .then((result) => {
        const credential = OAuthProvider.credentialFromResult(result);
        const microsoftUser = result.user;
        console.log(credential);
        console.log(microsoftUser);
        fetch('http://localhost:8000/microsoft/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: microsoftUser.providerData[0].email,
                    first_name: microsoftUser.displayName,
                    last_name: microsoftUser.displayName,
                    token: credential.accessToken,
                })
        })
        .then(response => response.json())
        .then(data => {
            localStorage.setItem('email', JSON.stringify(data.data.email));
            localStorage.setItem('first_name', JSON.stringify(data.data.first_name));
            localStorage.setItem('token', JSON.stringify(data.data.token));
            return true;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    }).catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = OAuthProvider.credentialFromError(error);

        console.log(errorCode, errorMessage, email, credential);
    });
    return false
}


export default microsoftLogin;