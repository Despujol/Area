
/**
 *  Permet d'afficher la bar en haut de la page avec le lien vers l'accueil, le login et le register
 * A importer dans chaque page
 * @returns 
 */

const Bar = () => {
    return (
        <div class="container"><div class="block-1"><a href='/' className='link'>Area-Type</a></div>
            <div class="block-2"><a href='/login' className='link'>Log in</a></div>
            <div class="block-3"><a href='/register' className='link'>Sign Up</a></div>
        </div>
    )
};

export default Bar;