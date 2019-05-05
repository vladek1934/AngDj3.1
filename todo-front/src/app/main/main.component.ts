import {Component, OnInit} from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {Tasklist, Task} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  constructor(private provider: ProviderService) {
  }
  public isLogged = false;
  public tasklists: Tasklist[] = [];
  public tasks: Task[] = [];
  public dispTask: Task;
  public loading = true;
  public taskloaded = false;
  public name: any = '';


  ngOnInit() {
    this.provider.getTasklists().then(
      res => {
        this.tasklists = res;
        this.loading = false;
      }
    );
  }

  getTasks(tasklist: Tasklist) {
    this.provider.getTasks(tasklist).then(res => {
      this.tasks = res;
    });

  }

  getTask(id: number) {
    this.provider.getTask(id).then(res => {
      this.dispTask = res;
      this.taskloaded = true;
    });
  }

  updateTasklist(c: Tasklist) {
    this.provider.updateTasklist(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  deleteTasklist(c: Tasklist) {
    this.provider.deleteTasklist(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getTasklists().then(r => {
        this.tasklists = r;
      });
    });
  }

  createTasklist() {
    if (this.name !== '') {
      this.provider.createTasklist(this.name).then(res => {
        this.name = '';
        this.tasklists.push(res);
      });
    }
  }

  updateTask(c: Task) {
    this.provider.updateTask(c).then(res => {
      console.log(c.name + ' updated');
    });
  }

  deleteTask(c: Task) {
    this.provider.deleteTask(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getTasks(c).then(r => {
        this.tasklists = r;
      });
    });
  }

  createTask() {
    if (this.name !== '') {
      this.provider.createTask(this.name).then(res => {
        this.name = '';
        this.tasklists.push(res);
      });
    }
  }

}
