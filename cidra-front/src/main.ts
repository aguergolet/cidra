import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter, RouterModule, withComponentInputBinding, withHashLocation } from '@angular/router';
import { provideHttpClient } from '@angular/common/http';
import { importProvidersFrom } from '@angular/core';
import { AppComponent } from './app/app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { HomeComponent } from './app/pages/home/home.component';
import { ToolDetailComponent } from './app/pages/tool-detail/tool-detail.component';
bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(
      [
        { path: '', redirectTo: 'home', pathMatch: 'full' },
        { path: 'home', component: HomeComponent },
        { path: 'tool', component: ToolDetailComponent },
        { path: 'tool/:id', component: ToolDetailComponent }
      ],
      withHashLocation(),
      withComponentInputBinding()
    ),
    provideHttpClient(),
    importProvidersFrom(
      BrowserAnimationsModule,
      MatSidenavModule,
      MatListModule,
      MatToolbarModule,
      MatIconModule,
      MatButtonModule,
      RouterModule.forRoot([])
    ),
  ],
}).catch(err => console.error(err));
