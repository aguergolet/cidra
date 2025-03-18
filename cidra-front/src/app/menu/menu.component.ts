import { Component, OnInit, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { ConfigService } from '../services/config.service';

interface Tool {
  id: string;
  title: string;
  description: string;
}

interface ConfigResponse {
  title: string;
  description: string;
  tools: Tool[];
}

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [
    CommonModule,
    RouterOutlet,
    RouterLink,
    MatSidenavModule,
    MatListModule,
    MatToolbarModule,
    MatIconModule,
    MatButtonModule
  ],
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
  tools: Tool[] = [];
  config = new ConfigService();
  readonly http = inject(HttpClient);
  readonly apiUrl = this.config.getApiUrl() + '/config'; 

  ngOnInit() {
    this.http.get<ConfigResponse>(this.apiUrl).subscribe(
      (data) => {
        this.tools = data.tools;
      },
      (error) => {
        console.error('Failed to load configuration', error);
      }
    );
  }
}
