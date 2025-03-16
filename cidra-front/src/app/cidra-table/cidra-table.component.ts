import { Component, Input, OnInit } from '@angular/core';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common'; // Import CommonModule

@Component({
  selector: 'app-cidra-table',
  imports: [MatTableModule, CommonModule], // Add CommonModule to imports
  templateUrl: './cidra-table.component.html',
  styleUrls: ['./cidra-table.component.css'] 
})
export class CidraTableComponent implements OnInit { // Adicionado `OnInit`
  @Input() data!: { title: string; headers: string[]; rows: any[][] };

  ngOnInit() {
    if (!this.data || !this.data.headers || !this.data.rows) {
      console.error('O payload fornecido é inválido.');
    }
  }
}
