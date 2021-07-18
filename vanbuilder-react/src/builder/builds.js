import React, {useEffect, useState}  from 'react'

import { apiBuildList } from './lookup'

export function BuildList() {
    const [builds, setBuilds] = useState([])
    const [buildsDidSet, setBuildsDidSet] = useState(false)
    useEffect(() => {
        if (buildsDidSet === false) {
            const handleBuildListLookup = (response, status) => {
                if (status === 200) {
                    setBuilds(response)
                    setBuildsDidSet(true)
                } else {
                    alert("There was an error")
                }
            }  
            apiBuildList(handleBuildListLookup)
        }
    }, [buildsDidSet, setBuildsDidSet])
    console.log(builds)

    return <div>

    </div>
}

export function BuildListItem(props) {
    const {build} = props
    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `build/${build.id}/components/`
    }
    return <div>
        </div>
}