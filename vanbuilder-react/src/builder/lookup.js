import {backendLookup} from '../lookup'


export function apiBuildCreate(newBuild, callback) {
    backendLookup("POST", '/build/create/', callback, newBuild)
}

export function apiBuildList(callback) {
    backendLookup("GET", '/build/list/', callback)
}

export function apiBuildSelect(Build, callback) {
    backendLookup("POST", '/build/select/', callback, Build)
}

export function apiVehicleList(callback) {
    backendLookup("GET", '/build/vehicles/', callback)
}

export function apiVehicleDetail(van_id, callback) {
    backendLookup("GET", `/build/vehicles/${van_id}/`, callback)
}

export function apiVehicleSelect(Vehicle, callback) {
    backendLookup("POST", '/build/vehicles/select/', callback, Vehicle)
}