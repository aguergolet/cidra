import { Injectable } from '@angular/core';
import * as dotenv from 'dotenv';
import { log } from 'node:console';

@Injectable({
    providedIn: 'root'
})
export class ConfigService {
    private apiUrl: string;
    private port: number;

    constructor() {
        dotenv.config( );
        log(process.cwd());

        this.apiUrl = process.env['API_URL'] || 'http://localhost';
        this.port = Number(process.env['API_PORT']) || 5000;
    }

    public getApiUrl(): string {
        return this.apiUrl + ':' + this.port;
    }   

    getPort(): number {
        return this.port;
    }
}