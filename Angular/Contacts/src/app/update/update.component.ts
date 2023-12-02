import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css'],
})
export class UpdateComponent {
  contactForm = this.formBuilder.group({
    FirstName: '',
    LastName: '',
    PhoneNo: '',
    emailID: '',
    CityName: '',
  });
  constructor(private formBuilder: FormBuilder) {}

  onSubmit(): void {}

  update() {
    window.alert('Contact has been updated!');
  }
}
