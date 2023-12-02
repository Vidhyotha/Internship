import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { ContactInfoComponent } from './contact-info/contact-info.component';
import { NewContactComponent } from './new-contact/new-contact.component';
import { UpdateComponent } from './update/update.component';

@NgModule({
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ContactListComponent },
      { path: 'contacts/:contactId', component: ContactInfoComponent },
      { path: 'addcontact', component: NewContactComponent },
      { path: 'update', component: UpdateComponent },
    ]),
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    ContactListComponent,
    ContactInfoComponent,
    NewContactComponent,
    UpdateComponent,
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
