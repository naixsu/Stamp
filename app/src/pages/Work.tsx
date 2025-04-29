import React from 'react';


export const Work:React.FC = () => {
    const electron = (window as any).electron;

    return (
        <div>
            This is work page content. <br />
            The home directory is @ {electron.homeDir()}. <br />
            The OS arch is {electron.arch()}. <br />
            The version is {electron.osVersion()}. <br />
            The name of the user is {electron.userInfo()}. <br />
        </div>
    );
};
