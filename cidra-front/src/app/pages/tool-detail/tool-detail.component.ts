import { Component, OnInit, inject, OnDestroy } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router, Params } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatError } from '@angular/material/form-field';
import {Tool } from '../../models/tool.model';
import { MatIcon } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
@Component({
  selector: 'app-tool-detail',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButtonModule, MatError, MatIcon, MatInputModule, FormsModule],
  templateUrl: './tool-detail.component.html',
  styleUrls: ['./tool-detail.component.css']
})
export class ToolDetailComponent implements OnInit, OnDestroy {

  toolId: string = '';
  toolConfig: Tool = new Tool();
  errorMessage: string = ''
  readonly http = inject(HttpClient);
  readonly route = inject(ActivatedRoute);
  readonly apiUrl = 'http://localhost:5000/getconfig';

  private routeSubscription: any;

  ngOnInit() {
    this.routeSubscription = this.route.params.subscribe((params: Params) => {
      this.toolId = params['id'];
      this.loadToolConfig();
    });
  }

  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
  }

  loadToolConfig() {
    this.http.get<Tool>(`${this.apiUrl}/${this.toolId}`).subscribe({
      next: (data) => {
        this.toolConfig = data;        
      },
      error: (error) => {
        console.error('Failed to load configuration', error);
        this.errorMessage = 'Failed to load configuration';
      }
    });
  }
}
