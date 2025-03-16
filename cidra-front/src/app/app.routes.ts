import { Routes } from '@angular/router';
import { ToolDetailComponent } from './pages/tool-detail/tool-detail.component';
import { HomeComponent } from './pages/home/home.component';

export const routes: Routes = [
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: 'home', component: HomeComponent },
    { path: 'tool', component: ToolDetailComponent },
    { path: 'tool/:id', component: ToolDetailComponent }
];