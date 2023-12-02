import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-new-contact',
  templateUrl: './new-contact.component.html',
  styleUrls: ['./new-contact.component.css'],
})
export class NewContactComponent {
  contactForm = this.formBuilder.group({
    FirstName: '',
    LastName: '',
    PhoneNo: '',
    emailID: '',
    CityName: '',
  });
  constructor(private formBuilder: FormBuilder) {}

  onSubmit(): void {}

  add() {
    window.alert('Contact has been added!');
  }
}
