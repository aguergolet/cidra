import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-cidra-label',
  templateUrl: './cidra-label.component.html',
  styleUrls: ['./cidra-label.component.css']
})
export class CidraLabelComponent {
  @Input() title!: string;
  @Input() content!: string;
}