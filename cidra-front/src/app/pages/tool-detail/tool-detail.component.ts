import { Component, OnInit, inject, OnDestroy } from '@angular/core';
import { ActivatedRoute, NavigationEnd, Router, Params } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatError } from '@angular/material/form-field';
import { Tool } from '../../models/tool.model';
import { MatIcon } from '@angular/material/icon';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { ConfigService } from '../../services/config.service';
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
  config = new ConfigService();
  errorMessage: string = ''
  readonly http = inject(HttpClient);
  readonly route = inject(ActivatedRoute);
  readonly apiUrl = this.config.getApiUrl() + '/getconfig';
  readonly commandUrl = this.config.getApiUrl() + "/runCommand"

  private routeSubscription: any;

  ngOnInit() {
    console.info('ToolDetailComponent initialized.');
    this.routeSubscription = this.route.params.subscribe((params: Params) => {
      this.toolId = params['id'];
      console.info(`Tool ID from route: ${this.toolId}`);
      this.errorMessage = '';
      this.loadToolConfig();
    });
  }

  ngOnDestroy() {
    this.routeSubscription.unsubscribe();
  }

  sendCommand() {
    console.info('Sending command with tool configuration:', this.toolConfig);
    this.http.post(`${this.commandUrl}`, this.toolConfig).subscribe({
      next: (response) => {
        console.info('Command executed successfully:', response);
        this.errorMessage = response.toString();
      },
      error: (error) => {
        console.error('Failed to execute command:', error);
        this.errorMessage = 'Failed to execute command ' + error.message;
      }
    });
  }

  loadToolConfig() {
    console.info(`Loading tool configuration for tool ID: ${this.toolId}`);
    this.http.get<Tool>(`${this.apiUrl}/${this.toolId}`).subscribe({
      next: (data) => {
        console.info('Tool configuration loaded successfully:', data);
        this.toolConfig = data;
      },
      error: (error) => {
        console.error('Failed to load configuration:', error);
        this.errorMessage = 'Failed to load configuration';
      }
    });
  }
}
