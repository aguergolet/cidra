import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CidraTableComponent } from './cidra-table.component';

describe('CidraTableComponent', () => {
  let component: CidraTableComponent;
  let fixture: ComponentFixture<CidraTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CidraTableComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CidraTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
