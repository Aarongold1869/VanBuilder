import React, {useEffect, useState}  from 'react'
import { BuildList } from './builds'

import arrowButton from '../icons/svgs/arrowButton.svg'

export function BuildListComponent(props) {
    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/builds/new-build/`
    }
    return <div className='centered' style={{marginTop:'20vh'}}>
        <div className='build-list-view-title'>
            <h1>Your Builds</h1>
            <a className='arrow-btn' onClick={handleLink}>Start New Build
                <img src={arrowButton}/>
            </a>
        </div>
        <hr/>
        <BuildList {...props} />
    </div>
}