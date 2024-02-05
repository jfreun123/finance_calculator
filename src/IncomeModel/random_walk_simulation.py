from IncomeModel.events_utils import Events
import torch
from torch import nn, optim

class Simulation:
    def __init__(self, starting_amount, curr_age, end_age, random_rate, savings_at_year, random_big_event):
        self.__total_iters = end_age - curr_age+1
        self.__starting_amount = starting_amount
        self.__event_helper = Events(curr_age=23,
                                     random_rate=random_rate, 
                                     savings_at_year=savings_at_year, 
                                     random_big_event=random_big_event)
        
        self.__device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
        self.N = 100  # num_samples_per_class
        self.D = 1  # dimensions
        self.C = 1  # num_classes
        self.H = 100  # num_hidden_units

        self.learning_rate = 1e-8
        self.lambda_l2 = 1e-5

    def single_simulation(self):
        results_per_year = [self.__starting_amount]
        curr_saved = self.__starting_amount
        success = True
        for iter in range(1, self.__total_iters):
            curr_saved = max(self.__event_helper.process_year(
                            iter=iter, starting_amount=curr_saved), 0)
            results_per_year.append(curr_saved)
            if (curr_saved <= 0): success = False
        return (results_per_year, success)
    
    def many_simulations(self, number_of_simulations):
        for _ in range(number_of_simulations):
            yield self.single_simulation()

    def deep_learning_linear_regression(self, number_of_simulations):
        X = self.__get_x_tensor()
        model = nn.Sequential(
            nn.Linear(self.D, self.H).float(),
            nn.Linear(self.H, self.C).float(),
        )
        model.to(self.__device)

        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=self.learning_rate, weight_decay=self.lambda_l2) # built-in L2

        data_points = self.many_simulations(number_of_simulations)
        y_data = []
        for (y_raw, _) in data_points:
            for t in range(self.N):
                y = torch.unsqueeze(torch.FloatTensor(y_raw), dim=1)
                y_data.append(y)
                y_pred = model(X)
                optimizer.zero_grad()
                loss = criterion(y_pred, y)
                print("[EPOCH]: %i, [LOSS or MSE]: %.6f" % (t, loss.item()))
                loss.backward()
                optimizer.step()
        
        return (y_data, model(X))
    
    def deep_learning_full(self, number_of_simulations):
        X = self.__get_x_tensor()
        self.learning_rate = 1e-0
        model = nn.Sequential(
            nn.Linear(self.D, self.H),
            nn.ReLU(),
            nn.Linear(self.H, self.C)
        )

        model.to(self.__device)
        criterion = torch.nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.learning_rate, weight_decay=self.lambda_l2) # built-in L2

        data_points = self.many_simulations(number_of_simulations)
        y_data = []
        for (y_raw, _) in data_points:
            for t in range(self.N):
                y = torch.unsqueeze(torch.FloatTensor(y_raw), dim=1)
                y_data.append(y)
                y_pred = model(X)
                optimizer.zero_grad()
                loss = criterion(y_pred, y)
                print("[EPOCH]: %i, [LOSS or MSE]: %.6f" % (t, loss.item()))
                loss.backward()
                optimizer.step()
        return (y_data, model(X))
            
    def __get_x_tensor(self):
        return torch.unsqueeze(torch.arange(0, self.__total_iters, dtype=torch.float32), dim=1).to(self.__device)

