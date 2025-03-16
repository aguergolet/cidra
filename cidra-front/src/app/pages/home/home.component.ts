import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { ConfigResponse } from '../../models/config-response.model';
import { MatCardModule } from '@angular/material/card';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule, MatCardModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  title = 'Loading...';
  description = '';
  readonly http = inject(HttpClient);
  readonly apiUrl = 'http://localhost:5000/config'; // ✅ Corrige a URL da API

  constructor(private readonly router: Router) {
    this.router.events.subscribe(event => console.log('Router Event:', event));
  }
  
  ngOnInit() {
    
    this.http.get<ConfigResponse>(this.apiUrl).subscribe({
      next: (data) => {
        this.title = data.title;
        this.description = data.description;
      },
      error: (error) => {
        console.error('Failed to load configuration', error);
      }
    });

}
}
