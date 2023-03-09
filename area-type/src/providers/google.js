import { signInWithPopup, GoogleAuthProvider } from "firebase/auth";
import auth from './../firebase';

const googleLogin = async () => {
    const provider = new GoogleAuthProvider();
    provider.addScope('openid, email, profile, https://www.googleapis.com/auth/gmail.readonly, https://www.googleapis.com/auth/gmail.send, https://www.googleapis.com/auth/drive, https://www.googleapis.com/auth/drive.file');
    provider.setCustomParameters({
        prompt: 'consent'
      });
      
    await signInWithPopup(auth, provider)
    .then((result) => {
        const credential = GoogleAuthProvider.credentialFromResult(result);
        const googleUser = result.user;
        console.log(credential);
        console.log(googleUser);
        fetch('http://localhost:8000/google/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: googleUser.providerData[0].email,
                    first_name: googleUser.displayName,
                    last_name: googleUser.displayName,
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
        const credential = GoogleAuthProvider.credentialFromError(error);

        console.log(errorCode, errorMessage, email, credential);
    });
    return false
}

export default googleLogin;