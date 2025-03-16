import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CidraLabelComponent } from './cidra-label.component';

describe('CidraLabelComponent', () => {
  let component: CidraLabelComponent;
  let fixture: ComponentFixture<CidraLabelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CidraLabelComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CidraLabelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
