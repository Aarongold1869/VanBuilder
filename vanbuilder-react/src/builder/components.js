import React, {useEffect, useState}  from 'react'
import { BuildList } from './builds'


export function BuildListComponent(props) {
    return <div className={props.className}>
        <BuildList {...props} />
    </div>
}