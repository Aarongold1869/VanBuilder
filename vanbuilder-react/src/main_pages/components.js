import React from 'react'
import logo from '../icons/logos/Logo.png'

export function LandingPage(props) {
    const handleBuilds = (event) => {
        event.preventDefault()
        window.location.href = `builds`
    }
    const handleLogin = (event) => {
        event.preventDefault()
        window.location.href = `login`
    }
    return <div className='centered'>
        <div class='row-10'>
            <div> 
                <img src={logo} alt="logo" style={{justifyContent:'end', alignItems:'center', marginBottom: 50}} />
            </div>
            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', marginBottom: 15}}> 
                <div class='butt outline-darkgreen' onClick={handleBuilds} >Start Building</div>
            </div>
            <div style={{display: 'flex',  justifyContent:'center', alignItems:'center', marginBottom: 15}}> 
                <div class='butt outline-darkgreen' onClick={handleLogin} >Login / Signup</div>
            </div>
        </div>
    </div>
}