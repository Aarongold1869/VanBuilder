import React, {useEffect, useState}  from 'react'

import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';

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

    return <div>
        {builds.map((item, index)=> {return <BuildListItem build={item} key={`${index}-{item.id}`} />})}
    </div>
}

export function BuildListItem(props) {
    const {build} = props
    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `build/${build.id}/components/`
    }
    return <div className='mt-3'>
        <Card border="salmon">
        <Card.Header >{build.build_title}</Card.Header>
        <Card.Body>
            <Card.Title>{build.vehicle_info}</Card.Title>
            <Card.Text>
                Budget: ${build.budget}
            </Card.Text>
            <Button variant='bluegreen' onClick={handleLink}>View Build</Button>
        </Card.Body>
        </Card>
    </div>
}