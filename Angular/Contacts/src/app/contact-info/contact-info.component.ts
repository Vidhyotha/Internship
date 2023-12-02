import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Contact, contacts } from '../contacts';

@Component({
  selector: 'app-contact-info',
  templateUrl: './contact-info.component.html',
  styleUrls: ['./contact-info.component.css'],
})
export class ContactInfoComponent implements OnInit {
  contact: Contact | undefined;
  constructor(private route: ActivatedRoute) {}

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const contactIDFromRoute = routeParams.get('contactId');

    this.contact = contacts.find(
      (contact) => contact._id === contactIDFromRoute
    );
  }
}
