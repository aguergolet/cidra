import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
    providedIn: 'root'
})
export class ConfigService {
    private apiUrl: string;
    private port: number;

    constructor() {
        

        this.apiUrl = environment.API_URL || 'http://localhost';
        this.port = environment.API_PORT || 3193;
    }

    public getApiUrl(): string {
        return this.apiUrl + ':' + this.port;
    }   

    getPort(): number {
        return this.port;
    }
}