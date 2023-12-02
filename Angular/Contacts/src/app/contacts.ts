export interface Contact {
  _id: string;
  FirstName: string;
  LastName: string;
  PhoneNo: number;
  emailID: string;
  CityName: string;
  Deleted: number;
}

export const contacts = [
  {
    _id: '64b617fe95a52272d4339207',
    FirstName: 'Vidhyotha',
    LastName: 'Shetty',
    PhoneNo: 8277040888,
    emailID: 'vidhyotha@gmail.com',
    CityName: 'Bangalore',
    Deleted: 0,
  },
  {
    _id: '64b61d52bb8be786d2200e30',
    FirstName: 'Sumukh',
    LastName: 'Shetty',
    PhoneNo: 9611420391,
    emailID: 'sumukh@gmail.com',
    CityName: 'Bangalore',
    Deleted: 0,
  },
  {
    _id: '64b67481404ea14186384202',
    FirstName: 'Yogish',
    LastName: 'Kumar',
    PhoneNo: 9341211376,
    emailID: 'yogshetty@gmail.com',
    CityName: 'Bangalore',
    Deleted: 0,
  },
];
