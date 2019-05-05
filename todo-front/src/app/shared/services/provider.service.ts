import {EventEmitter, Injectable} from '@angular/core';
import {MainService} from './main.service';
import {Task, Tasklist} from '../models/models';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTasklists(): Promise<Tasklist[]> {
    return this.get('http://localhost:8000/api/task_lists', {});
  }

  getTasks(tasklist: Tasklist): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/task_lists/${tasklist.id}/tasks`, {});
  }

  getTask(id: number): Promise<Task> {
    return this.get(`http://localhost:8000/api/tasks/${id}`, {});
  }

  createTask(name: any): Promise<Task> {
    return this.post('http://localhost:8000/api/tasks/', {
      name: name
    });
  }

  updateTask(category: Task): Promise<Task> {
    return this.put(`http://localhost:8000/api/tasks/${category.id}/`, {
      name: category.name
    });
  }

  deleteTask(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasks/${id}/`, {});
  }

  createTasklist(name: any): Promise<Tasklist> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: name
    });
  }

  updateTasklist(tasklist: Tasklist): Promise<Tasklist> {
    return this.put(`http://localhost:8000/api/task_lists/${tasklist.id}/`, {
      name: tasklist.name
    });
  }

  deleteTasklist(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }
}


