import { Routes } from '@angular/router';
import { ToolDetailComponent } from './pages/tool-detail/tool-detail.component';
import { HomeComponent } from './pages/home/home.component';
import { RenderMode } from '@angular/ssr';

export const DEFAULT_RENDER_MODE = 'default';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'tool', component: ToolDetailComponent },
    { path: 'tool/:id', component: ToolDetailComponent, data: { renderMode: DEFAULT_RENDER_MODE }}
];