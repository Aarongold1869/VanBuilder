import React from 'react'
import logo from '../icons/logos/Logo.png'
import arrowButton from '../icons/svgs/arrowButton.svg'

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
        <img className='main-logo' src={logo} alt="van builter logo" />
        <div className='btn-group'>
            <a className='arrow-btn' onClick={handleBuilds} >Start Building 
                <img src={arrowButton}/>
            </a>
            <a className='arrow-btn' onClick={handleLogin} >Login / Signup
                <img src={arrowButton}/>
            </a>
        </div>
    </div>
}