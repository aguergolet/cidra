import { Component, OnInit, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { Router } from '@angular/router';
import { MenuComponent } from './menu/menu.component';
import { ConfigResponse } from './models/config-response.model';




@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    MatSidenavModule,
    MatListModule,
    MatToolbarModule,
    MatIconModule,
    MenuComponent,
    MatButtonModule
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Loading...';
  description = '';
  tools: any[] = [];
  readonly http = inject(HttpClient);
  readonly apiUrl = 'http://localhost:5000/config'; // ✅ Corrige a URL da API

  constructor(private router: Router) {
    this.router.events.subscribe(event => console.log('Router Event:', event));
  }
  
  ngOnInit() {
    
    this.http.get<ConfigResponse>(this.apiUrl).subscribe(
      (data) => {
        this.title = data.title;
        this.description = data.description;
        this.tools = data.tools;
      },
      (error) => {
        console.error('Failed to load configuration', error);
      }
    );
  }
}
