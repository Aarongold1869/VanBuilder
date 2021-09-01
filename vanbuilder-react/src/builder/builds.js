import React, {useEffect, useState}  from 'react'

import { apiBuildList } from './lookup'

export function BuildList() {
    const [builds, setBuilds] = useState([])
    const [buildsDidSet, setBuildsDidSet] = useState(false)
    const [hasBuilds, setHasBuilds] = useState(true)
    useEffect(() => {
        if (buildsDidSet === false) {
            const handleBuildListLookup = (response, status) => {
                if (status === 200) {
                    setBuilds(response)
                    setBuildsDidSet(true)
                } else if (status === 204) {
                    setHasBuilds(false)
                } else {
                    alert("There was an error")
                }
            }  
            apiBuildList(handleBuildListLookup)
        }
    }, [buildsDidSet, setBuildsDidSet, hasBuilds, setHasBuilds])

    return <div className='build-list-container'>{(hasBuilds === true) && <div>
        {builds.map((item, index)=> {return <BuildListItem build={item} key={`${index}-{item.id}`} />})}
    </div>} 
    {(hasBuilds === false) && <h3>You haven't created a build yet!</h3>}
    </div>
    
    
}

export function BuildListItem(props) {
    const {build} = props
    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/builds/${build.id}/`
    }
    return <div className='build-list-item' onClick={handleLink}>
        <div className='build-list-item-content'>
            <div className='build-list-item-content-text'>
                <h3>{build.build_title}</h3>
                <p>Van:&emsp;{build.vehicle_info}</p>
                <p>Budget:&emsp;${build.budget}</p>
                <p>Last Updated:&emsp;{build.last_updated}</p>
            </div>
            <img src={build.image}/>
        </div>
    </div>
}